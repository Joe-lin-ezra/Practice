const path = require('path');
const config = require(path.join(__dirname, '..', 'auth.config.js'));
const db = require(path.join(__dirname, '..', 'models'));
const User = db.user;
const Role = db.role;
const Op = db.Sequelize.Op;
const jwt = require("jsonwebtoken");
const bcrypt = require("bcryptjs");

async function signUp(req, res) {
    try {
        const user = await User.create({
            username: req.body.username,
            password: bcrypt.hashSync(req.body.password, 8),
            email: req.body.email,
            phoneNumber: req.body.phoneNumber
        });
        if(user) {
            res.status(200).send('User registered successfully.');
        }
    } catch (err) {
        res.status(500).send(err.message);
    }
}

async function signIn(req, res) {
    try{
        const user = await User.findOne({
            where: {
                username: req.body.username
            }
        });
        if(user) {
            res.status(404).send('Username not found.');
        }

        const passwordValid = bcrypt.compareSync(
            user.password,
            req.body.password
        );
        if (!passwordValid) {
            res.status(401).send('Password is incorrect.');
        }

        const token = jwt.sign({ id: user.id }, config.JWT_SECRET_KEY, {
            expiresIn: 86400
        });

        let authorization = "Bearer " + jwt;
        req.headers.authorization = authorization;
        res.status(200).send('Login success');

    } catch (err) {
        res.status(500).send(err.message);
    }

}

async function signOut(req, res) {
    
}


export default {
    signUp,
    signIn,
    signOut,
}