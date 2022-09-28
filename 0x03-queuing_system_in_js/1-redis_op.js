import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server: ', err));

client.on('connect', () => console.log('Redis client connected to the server'));

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value);
}

const displaySchoolValue = (schoolName) => {
  client.get(schoolName);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
