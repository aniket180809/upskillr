const router = require("express").Router();
const axios = require("axios");

router.get("/recommend", async (req, res) => {
  try {
    const { skill } = req.query;
    const response = await axios.post("http://localhost:5001/recommend", { skill });
    res.json(response.data);
  } catch (err) {
    res.status(500).json({ error: "Recommendation service failed" });
  }
});

module.exports = router;
