import axios from 'axios';

// const BASE_URL = 'http://doc.duckdake.com:8054/'
const BASE_URL = 'http://192.168.50.74:3000/'


const fetch = axios.create({
    baseURL: BASE_URL,
    headers: {
      'Content-Type': 'multipart/form-data',
    },
    // responseType: 'blob',  下载文件
    timeout: 30 * 60 * 60 * 1000,
  });


  fetch.interceptors.response.use(
    (response) => {
      const data = response.data;
      return data
    },
    error => {
      return Promise.reject(error);
    },
  );


export default fetch;
