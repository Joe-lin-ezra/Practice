export default (sequelize, Sequelize) => {
    const User = sequelize.define('users', {
        username: {
            type: Sequelize.STRING,
        },
        password: {
            type: Sequelize.STRING,
        },
        email: {
            type: Sequelize.STRING,
        },
        phoneNumber: {
            type: Sequelize.STRING,
        }
    });
    return User;
}