import axios from 'axios';


export async function get_donation(id) {
    return (await axios.get("/api/get/donation", {params: {id}})).data[0];
}


export async function get_product(id) {
    return (await axios.get("/api/get/product", {params: {id}})).data[0];
}


export async function get_products() {
    return (await axios.get("/api/get/product/available")).data;
}


export async function get_latest_donations(timestamp) {
    return (await axios.get("/api/donate/latest", {params: {timestamp}})).data;
}

export default { get_product, get_products, get_donation, get_latest_donations }
