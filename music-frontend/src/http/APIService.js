import axios from 'axios';
const API_URL = 'https://8380s22tm5app.com/';

export class APIService {
    constructor() {

    }

    authenticateLogin(credentials) {
        const url = `${API_URL}api/token/`;
        const logFormData = new FormData();
        logFormData.append("username", credentials.username);
        logFormData.append("password", credentials.password);
        return axios.post(url,logFormData);
    }

    authenticateSignup(signupcreds) {
        const url = `${API_URL}api/signup/`;
        const logFormData = new FormData();
        logFormData.append("first_name", signupcreds.first_name);
        logFormData.append("last_name", signupcreds.last_name);
        logFormData.append("email", signupcreds.email);
        logFormData.append("username", signupcreds.username);
        logFormData.append("password", signupcreds.password);
        return axios.post(url,logFormData);
    }
}