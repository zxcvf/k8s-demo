import fetch from './request';

export function HelloAPI(text, file) {
    let url = '';
    let formData = new FormData();
//    formData.append('text', text);
//    formData.append('file', file);

    return fetch.get(url, formData);
};
