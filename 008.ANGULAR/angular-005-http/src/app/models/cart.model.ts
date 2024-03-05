import { Product } from "./product.models";

export interface Cart{
    id: number;
    //Many To One
    userId: number;
    date: Date;
    //One to Many
    products: ProductCart[];
}

export interface ProductCart {
    productId: number;
    quantity: number;
}
