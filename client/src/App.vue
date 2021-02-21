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
        <the-main-game
          @on-begin-game="sendRequest"
          :cards="cardsData"
          :isLoading="isLoading"></the-main-game>
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
      cardsData: [
        {value: 'C', path: require('./assets/cherry.svg')},
        {value: 'L', path: require('./assets/lemon.svg')},
        {value: 'O', path: require('./assets/orange.svg')}
      ],
      isLoading: false,
    };
  },
  methods: {
    sendRequest() {
      // TODO: SEND REQUEST TO BACK
      this.isLoading = true;
    }
  }
};
</script>
