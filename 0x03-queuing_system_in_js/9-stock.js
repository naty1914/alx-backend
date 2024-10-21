#!/usr/bin/yarn dev
const express = require('express');
const redis = require('redis');
const { promisify } = require('util');


const app = express();
app.use(express.json());

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

function getItemById(id) {
  return listProducts.find((item) => item.id === id);
}

async function reserveStockById(id, stock) {
  const key = `item.${id}`;
  const currentStock = await getAsync(key);

  if (currentStock) {
    const newStock = parseInt(currentStock) - stock;
    await setAsync(key, newStock);
    return newStock;
  }

  return null;
}

async function getCurrentReservedStockById(id) {
  const key = `item.${id}`;
  const currentStock = await getAsync(key);

  if (currentStock) {
    return parseInt(currentStock);
  }

  return null;
}

app.get('/list_products', async (req, res) => {
  const products = listProducts.map((item) => ({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
  }));

  res.json(products);
});

app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const item = getItemById(itemId);

  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = currentStock !== null ? item.stock - currentStock : item.stock;

  res.json({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity,
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const item = getItemById(itemId);

  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }

  const currentStock = await getCurrentReservedStockById(itemId);

  if (currentStock === null || currentStock < 1) {
    res.json({ status: 'Not enough stock available', itemId });
    return;
  }

  await reserveStockById(itemId, 1);

  res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});