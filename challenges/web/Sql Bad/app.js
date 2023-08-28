const express = require('express');
const app = express();
app.use(express.json());
app.use(express.urlencoded());

const mongodb = require('mongodb');
const MongoClient = mongodb.MongoClient;
const mongoURL = 'mongodb://mongodb:27017';

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/login.html');
});

app.post('/', async (req, res) => {
  const { username, password } = req.body;
  console.log(username,password);
  console.log(req.body);
  try {
    const user = await req.app.locals.db.findOne({ username, password });

    if (user) {
      res.status(200).json({ message: 'Login successful' });
    } else {
      res.status(401).json({ message: 'Invalid username or password' });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'An error occurred' });
  }
});

app.listen(3000, async () => {
  const client = await MongoClient.connect(mongoURL, err => {
    if(err) throw err;
    console.log('Connected to database');
  });
  const db = client.db('app').collection('users');
  await db.drop();
  await db.insertOne({
    username: 'admin',
    password: 'greyhats{n0sq1_sti11_c4n_1nj3ct!}'
  }, (err, res) => {
    if (err) throw err;
    console.log('Admin account added');
  });
  app.locals.db = db;
  console.log('Server is up');
});
