<template>
  <div class="loader" :style="loadingStyle">Loading...</div>
</template>

<script>
export default {
    props: {
        width: {
            type: String,
            default: '4em',
        },
        heigth: {
            type: String,
            default: '4em',
        },
    },
    computed: {
        loadingStyle() {
            return {
                '--loading-width': this.width,
                '--loading-height': this.heigth === this.width ? this.heigth : this.width,
            };
        },
    },
};
</script>

<style scoped>
.loader,
.loader:after {
    border-radius: 50%;
    width: var(--loading-width);
    height: var(--loading-height);
}
.loader {
    margin: auto auto;
    font-size: 10px;
    position: relative;
    text-indent: -9999em;
    border-top: 0.6em solid rgba(255, 255, 255, 0.2);
    border-right: 0.6em solid rgba(255, 255, 255, 0.2);
    border-bottom: 0.6em solid rgba(255, 255, 255, 0.2);
    border-left: 0.6em solid #FF9012;
    -webkit-transform: translateZ(0);
    -ms-transform: translateZ(0);
    transform: translateZ(0);
    -webkit-animation: load 1.1s infinite linear;
    animation: load 1.1s infinite linear;
}

@-webkit-keyframes load {
    0% {
        -webkit-transform: rotate(0deg);
        transform: rotate(0deg);
    }
    100% {
        -webkit-transform: rotate(360deg);
        transform: rotate(360deg);
    }
}

@keyframes load {
    0% {
        -webkit-transform: rotate(0deg);
        transform: rotate(0deg);
    }
    100% {
        -webkit-transform: rotate(360deg);
        transform: rotate(360deg);
    }
}
</style>
