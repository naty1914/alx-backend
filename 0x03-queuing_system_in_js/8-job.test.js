#!/usr/bin/yarn test
import sinon from 'sinon';
import { expect } from 'chai';
import { createQueue } from 'kue';
import createPushNotificationsJobs from './8-job.js';


describe('createPushNotificationsJobs', () => {
    const BIG_BROTHER = sinon.spy(console);
    const QUEUE = createQueue({ name: 'push_notification_code_test' });

    before(() => {
        QUEUE.testMode.enter(true);
    });

    after(() => {
        QUEUE.testMode.clear();
        QUEUE.testMode.exit();
    });
    afterEach(() => {
        BIG_BROTHER.log.resetHistory();
    });
    it('displays an error message if jobs is not an array', () => {
        expect(
            createPushNotificationsJobs.bind(createPushNotificationsJobs, {}, QUEUE)
        ).to.throw('Jobs is not an array');
    });
    it('adds jobs to the queue with the correct type', (done) => {
        expect(QUEUE.testMode.jobs.length).to.equal(0);
        const jobInfos = [
            {
                phoneNumber: '44556677889',
                message: 'Use the code  1982 to verify your account',
            },
            {
                phoneNumber: '98877665544',
                message: 'Use the code  1738 to verify your account',
            },
        ];

        createPushNotificationsJobs(jobInfos, QUEUE);
        expect(QUEUE.testMode.jobs.length).to.equal(2);
        done();
    });

    it('registers the success event handler for a job', (done) => {
        QUEUE.testMode.jobs[0].addListener('success', () => {
            expect(
                BIG_BROTHER.log
                    .calledWith('Notification job', QUEUE.testMode.jobs[0].id, 'completed')
            ).to.be.true;
            done();
        });
        QUEUE.testMode.jobs[0].emit('success');
    });

    it('registers the failed event handler for a job', (done) => {
        QUEUE.testMode.jobs[1].addListener('failed', () => {
            expect(
                BIG_BROTHER.log
                    .calledWith('Notification job', QUEUE.testMode.jobs[1].id, 'failed')
            ).to.be.true;
            done();
        });
        QUEUE.testMode.jobs[1].emit('failed');
    });

    it('registers the complete event handler for a job', (done) => {
        QUEUE.testMode.jobs[1].addListener('complete', () => {
            expect(
                BIG_BROTHER.log
                    .calledWith('Notification job', QUEUE.testMode.jobs[1].id, 'completed')
            ).to.be.true;
            done();
        });
        QUEUE.testMode.jobs[1].emit('complete');
    });

    it('registers the progress event handler for a job', (done) => {
        QUEUE.testMode.jobs[1].addListener('progress', () => {
            expect(
                BIG_BROTHER.log
                    .calledWith('Notification job', QUEUE.testMode.jobs[1].id, '25% complete')
            ).to.be.true;
            done();
        });
        QUEUE.testMode.jobs[1].emit('progress', 25);
    });
            
});
