import { AnyBulkWriteOperation, Document } from 'mongodb';




/**
 * Stores plant data in MongoDB.
 * @param plantsData - The plants info to store.
 * @returns A Promise that resolves when the plants info are stored successfully.
 */
//async function storeBasicPriceData(plantsData: any[]): Promise<void> {
try {
await mongoClient.connect();
const database = mongoClient.db(config.mongoDBName);
const collection = database.collection("prices");

// Bulk write upsert operations
var operations: AnyBulkWriteOperation<Document>[] = [];

plantsData.forEach((plantData: any) => {
    const updateFilter = { id: plantData.id }
    const updateDoc = {
    $set: plantData,
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

