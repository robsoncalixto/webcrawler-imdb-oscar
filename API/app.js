import express from "express";
const app = express();

const sequelize = new Sequelize('sqlite::memory:');

try {
    await sequelize.authenticate();
    console.log('Connection has been established successfully.');
  } catch (error) {
    console.error('Unable to connect to the database:', error);
  }

app.listen(3452, function () {
    console.log("link: http://localhost:3452");
})