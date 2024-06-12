import { AnyBulkWriteOperation, Document } from 'mongodb';




/**
 * Stores plant data in MongoDB.
 * @param priceData - The price info to store.
 * @returns A Promise that resolves when the price info are stored successfully.
 */
//async function storeBasicPriceData(plantsData: any[]): Promise<void> {
try {
await mongoClient.connect();
const database = mongoClient.db(config.mongoDBName);
const collection = database.collection("prices");

// Bulk write upsert operations
var operations: AnyBulkWriteOperation<Document>[] = [];
priceData.forEach((priceData: any) => {
    const updateFilter = { id: priceData.id }
    const updateDoc = {
    $set: priceData,
    $setOnInsert: { created_at: new Date() }
    };
    operations.push({
    updateOne: {
        filter: updateFilter,
        update: updateDoc,
        upsert: true
    }
    });
})

const result = await collection.bulkWrite(operations);
console.log("Price data stored in MongoDB successfully!", result);
} catch (error) {
console.error("Error storing price data in MongoDB", error);
throw new Error("Failed to fetch price data");
} finally {
await mongoClient.close();
}
//}

