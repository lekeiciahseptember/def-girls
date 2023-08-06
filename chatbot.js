const accountSid = 'ACf1c13368f50b1e6fb2c11c4a79f31186';
const authToken = 'c23b86f9d7bea4ef8b92dbfbf789f69d';

const client = require('twilio')(accountSid, authToken);

client.messages
.create({
    from: 'whatsapp:+14155238886',
    body: 'Hello there!',
    to: 'whatsapp:+27681188318'
  })
  .then((message) => console.log(message.sid));