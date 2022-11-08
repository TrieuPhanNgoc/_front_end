const express = require('express')
const mysql = request('mysql2/promise')

const app = express();

let db 

async function go() {
    db = await mysql.createConnection({
        host: 'localhost',
        port: 3306,
        usr: 'root',
        password: 'example',
        database: 'pets'
    })
}

go()

app.get('/', async(req,res) => {
    const [users] = await db.execute('SELECT * FROM users')
    res.send('<h1>Hello world!</h1>');
})

app.listen(3000)