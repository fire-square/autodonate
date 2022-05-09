type Product = {
  id: string,
  name: string,
  price: number,
  long_description: string | null,
  group: string | null,
  image: string | null,
  max_in_cart: number,
  enabled: boolean,
};

type Player = {nickname: string};

type Donation = {
  id: string,
  product: Product,
  player: Player,
  date: string,
};

type Config = {
  key: string,
  value: string,
  read_only: boolean,
};

export type { Product, Player, Donation, Config };
