<template>
  <div class="icon-container">
    <v-icon>mdi-currency-btc</v-icon>
    <h6>{{ credits }} Credits</h6>
  </div>
</template>

<script>
/**
 * Component to show the credits that the user have
 *** Needs to be encapsulate in a container with position relative
 **  Just have one props credits -> Number type 
 */
export default {
  name:'the-credit-button',
  props: {
    credits: {
      type: Number,
      required: true,
    }
  }
}
</script>

<style scoped>
.icon-container {
  display: grid;
  grid-template-columns: 1.5em 1fr;
  align-items: center;
  position: absolute;
  bottom: 1.5em;
  right: 1.7em;
  padding: .5em;
  border: 1px solid #606060;
  border-radius: 1em;
}
.icon-container > h6 {
  color: #747474;
}
</style>