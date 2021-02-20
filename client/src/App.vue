<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark>
      <h1 class="d-flex align-center">
        Jackpot Online
      </h1>

      <v-spacer></v-spacer>

      <v-btn text>
        <h3 class="mr-2">New Game</h3>
        <v-icon>mdi-gamepad</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <aside style="position: relative; height: 100%">
        <the-main-game></the-main-game>
        <the-credit-button :credits="clientCredits"></the-credit-button>
      </aside>
    </v-main>
  </v-app>
</template>

<script>
import TheMainGame from './components/TheMainGame.vue';
import TheCreditButton from './components/TheCreditButton.vue';

export default {
  name: 'App',
  components: {
    TheMainGame,
    TheCreditButton,
  },
  data() {
    return {
      clientCredits: 10, 
    };
  },
};
</script>
