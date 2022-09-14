const express = require('express');
const app = express();
const port = '8080';

/*const sequelize = new Sequelize('sqlite::memory:');
try {
    await sequelize.authenticate();
    console.log('Connection has been established successfully.');
  } catch (error) {
    console.error('Unable to connect to the database:', error);
  }
*/

app.get('/', (req, res) => {
  res.send('My first route');
})

app.listen(port,  () => {
  console.log(`app listening on port:${port}`);
});