export class App {
    private event: any;
    constructor(event: any) {
        this.event = event;
    }
    public start(): any {
        const body = JSON.stringify(
            {
                message: 'Go Serverless v1.0! Your function executed successfully!',
                input: this.event,
            },
            null,
            2
        )
        return {
            statusCode: 200,
            body: body,
        };       
    }
}