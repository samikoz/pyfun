const express = require('express')
const app = express();
const port = 8000;

app.use(express.static('static_files'));
app.listen(port);