const path = require('path');
const config = require(path.join(__dirname, '..', 'config', 'mysqldb.config.js'));
const Sequelize = require('sequelize');

const sequelize = new Sequelize(
    config.DB,
    config.USER,
    config.PASSWORD,
    {
        host: 'localhost',
        dialect: config.dialect,
        pool: {
            max: config.pool.max,
            min: config.pool.min,
            acquire: config.pool.acquire,
            idle: config.pool.idle
        }
    }
);

try {
    await sequelize.authenticate();
    console.log('Connection has been established successfully.');
} catch (error) {
    console.error('Unable to connect to the database:', error);
}

const db = {};
db.Sequelize = Sequelize;
db.sequelize = sequelize;

db.user = require(path.join(__dirname,'..', 'models', 'user.model.js'))(sequelize, Sequelize);
db.role = require(path.join(__dirname,'..', 'models', 'role.model.js'))(sequelize, Sequelize);

db.role.belongsToMany(db.user, {
  through: 'user_roles',
  foreignKey: 'roleId',
  otherKey: 'userId'
});
db.user.belongsToMany(db.role, {
  through: 'user_roles',
  foreignKey: 'userId',
  otherKey: 'roleId'
});

db.ROLES = ["user", "admin", "moderator"];
module.exports = db;
