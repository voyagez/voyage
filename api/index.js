import express from "express"
import dotenv from "dotenv"
import mongoose from "mongoose"
import authRoute from "./routes/auth.js"
import hotelsRoute from "./routes/hotels.js"
import roomsRoute from "./routes/rooms.js"
import usersRoute from "./routes/users.js"
const app = express()
dotenv.config()

const connect = async () => {
    try {
        await mongoose.connect(process.env.MONGO);
        console.log('Connected to mongoDB.')
    } catch (error) {
        throw error;
    }
}

app.get('/', (req,res)=>{
    res.send("hello")
})

app.use(express.json())

app.use("/auth", authRoute)
app.use("/hotels", hotelsRoute)
app.use("/rooms", roomsRoute)
app.use("/users", usersRoute)

app.listen(8800, ()=>{
    connect()
    console.log('Connected to backend')
})