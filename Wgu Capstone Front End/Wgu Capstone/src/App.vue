<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';

interface PredictionRequest {
  bedrooms: Number,
  bathrooms: Number,
  sqft_living: Number,
  sqft_lot: Number,
  floors: Number,
  sqft_above: Number,
  sqft_basement: Number,
  yr_built: Number
}

let error= ref('');

let prediction = ref('')

let bedrooms = ref('');
let bathrooms = ref('');
let sqftLiving = ref('');
let lotSize = ref('');
let floors = ref('');
let sqftAbove = ref('');
let sqftBasement = ref('');
let yearbuilt = ref('');

async function getPrediction() {
  error.value = '';
  prediction.value = '';

  if (!bedrooms.value || 
  !bathrooms.value || 
  !sqftLiving.value || 
  !lotSize.value || 
  !floors.value || 
  !sqftAbove.value || 
  !sqftBasement.value || 
  !yearbuilt.value) {
    error.value = 'All data must be input';
    return;
  }
  if (isNaN(Number(bedrooms.value)) || 
  isNaN(Number(bathrooms.value)) || 
  isNaN(Number(sqftLiving.value)) || 
  isNaN(Number(lotSize.value)) || 
  isNaN(Number(floors.value)) || 
  isNaN(Number(sqftAbove.value)) || 
  isNaN(Number(sqftBasement.value)) || 
  isNaN(Number(yearbuilt.value))) {
    error.value = 'All data must be numeric';
    return;
  }

  let predictionRequest: PredictionRequest = {
    bedrooms: +bedrooms.value,
    bathrooms: +bathrooms.value,
    sqft_living: +sqftLiving.value,
    sqft_lot: +lotSize.value,
    floors: +floors.value,
    sqft_above: +sqftAbove.value,
    sqft_basement: +sqftBasement.value,
    yr_built: +yearbuilt.value
  }
  
  const response = await axios.post<Number>("http://localhost:8000/predict", predictionRequest);

  if (response.status !== 200) {
    error.value = "Uknown error while trying to get prediction. Please try again."
    return;
  }

  prediction.value = response.data.toString();
}



</script>

<template>
  <div class="flexbox">
    <h2>Bedrooms</h2>
    <input v-model="bedrooms">
    <h2>Bathrooms</h2>
    <input v-model="bathrooms">
    <h2>Square Feet Living</h2>
    <input v-model="sqftLiving">
    <h2>Lot Size in Square Feet</h2>
    <input v-model="lotSize">
    <h2>Floors</h2>
    <input v-model="floors">
    <h2>Square Feet Above Ground</h2>
    <input v-model="sqftAbove">
    <h2>Basement Square Feet</h2>
    <input v-model="sqftBasement">
    <h2>Year Built</h2>
    <input v-model="yearbuilt">
    <button style="margin-top: 1rem; height: 2rem; border-radius: px;" @click="getPrediction" type="submit">Make Prediction</button>
    <h1 v-if="prediction">${{ prediction }}</h1>
    <h2 v-if="error">{{ error }}</h2>
    <div  class="images"> 
      <img class="image" src="./assets/actual_vs_prediction.png">
        <img class="image" src="./assets/p.png">
        <img class="image" src="./assets/r.png">
    </div>
  </div> 
</template>

<style scoped>
.image {
  height: 100%;
  width: 33%;
}
.images {
  display: flex;
  width: 100%;
}
.flexbox {
  display: flex;
  height: 100vh;
  width: 100%;
  flex-direction: column;
  align-items: center;
}
.title {
  margin-top: 10px;
}
.input {
  display: block;
  width: 20%;
}
</style>
