import axios from "axios";
import {baseURL} from "../constants/urls";

const apiService = axios.create({baseURL})

apiService.interceptors.request.use(request =>{
    const access_token = localStorage.getItem('access');

    if (access_token){
        request.headers.Authorization = `Bearer ${access_token}`
    }

    return request
})

export {apiService}