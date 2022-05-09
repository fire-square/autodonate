import axios from 'axios';


export async function get(url: string): Promise<any> {
    return (await axios.get(url)).data;
}

export default { get }
