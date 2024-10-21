#!/usr/bin/yard dev
import { createQueue } from 'kue';


const queue = createQueue();

const sendNotification = (phoneNumber, message) => {
    console.log(
        `Sending notification to ${phoneNumber},`,
        'with message:',
        message,
    );
};


queue.process('push_notification_code', 2, (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
});