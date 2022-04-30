import axios from 'axios';


export async function get(url) {
    return (await axios.get(url)).data;
}

export default { get }
