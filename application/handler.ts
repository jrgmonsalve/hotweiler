import { Handler } from 'aws-lambda';
import { App } from './App';

export const talk: Handler = (event: any) => {
    const app = new App(event);
    const response = app.start();
    return new Promise((resolve) => {
        resolve(response)
    })
}