const PROXY_CONFING = [
    {
        context: ['/token', '/api'],
        target: 'http://localhost:8000',
        secure: false
    }
];
module.exports = PROXY_CONFING;
