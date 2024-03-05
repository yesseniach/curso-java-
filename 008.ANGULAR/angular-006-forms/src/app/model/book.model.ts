export interface Book {
    id: number;
    title: string;
    price: number;
    available: boolean;
    publishdate: Date;
    //se utiliza para Selectores
    category: string;
    topics: string[];
}