import { Author } from "./author.model";
import { Editorial } from "./editorial.model";

export interface Book{
[x: string]: any;
    id: number;
    title: string;
    isbn: string;
    price: number;
    published: boolean;
    releaseDate: Date;
    author: Author;
    editorial: Editorial;
}