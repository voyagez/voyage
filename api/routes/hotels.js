import express from "express"

const router = express.Router()

//create
router.post('/', (req,res)=>{
    
})
//update
//delete
//get
//get all


router.get('/', (req, res)=>{
    res.send('hello, this is hotels endpoint')
})

export default router