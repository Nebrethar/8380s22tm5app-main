import axios from 'axios';
const API_URL = 'https://8380s22tm5app.com/';

export class APIService {
    constructor() {

    }

    authenticateLogin(credentials) {
        const url = `${API_URL}api/token/`;
        return axios.post(url, {
            auth: {
              username: credentials.username,
              password: credentials.password
            }
          });
    }
}