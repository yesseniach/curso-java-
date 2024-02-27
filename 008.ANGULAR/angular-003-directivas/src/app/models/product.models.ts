import { Manufacturer } from "./manufacturer.models";

export interface Product {
id: number;
title: string;
price: number;
available: boolean;
publishDate: Date;
//Many To One
manufacturer: Manufacturer;
}

