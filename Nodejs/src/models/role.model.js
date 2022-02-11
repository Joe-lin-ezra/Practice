export default (sequelize, Sequelize) => {
    const Role = sequelize.define('roles', {
        id: {
            type: Sequelize.INTEGER,
            autoIncrement: true,
            primaryKey: true,
        },
        name: {
            type: sequelize.STRING,
        }
    });
    return Role;
}