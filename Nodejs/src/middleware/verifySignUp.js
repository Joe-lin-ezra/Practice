const path = require('path');
const db = require(path.join(__dirname, '..', 'models', 'index.js'));
const ROLES = db.ROLES;
const User = db.user;

checkDuplicateUsernameOrEmail = async (req, res, next) => {
    try {
        // find for used username
        let user = await User.findOne({ 
            where: {
                username: req.body.username
            }
        });
        if(user) {
            return res.status(400).send('Duplicate username');
        }
        // find for used email
        user = await User.findOne({
            where: {
                email: req.body.email
            }
        });
        if(user) {
            return res.status(400).send('Duplicate email');
        }
        
        next();
    } catch (err) {
        res.status(500).send('Invalid username or email duplicate email');
    }
}

checkRolesExisted = async (req, res, next) => {
    // if(req.user.roles) {
        
    // }
    next();
}

export default {
    checkDuplicateUsernameOrEmail,
    checkRolesExisted
}