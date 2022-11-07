<template>
    <ion-page>
      <ion-header :translucent="true">
        <ion-toolbar>
          <ion-title>Camera Test</ion-title>
        </ion-toolbar>
      </ion-header>
      
      <ion-content :fullscreen="true">
        <ion-header collapse="condense">
          <ion-toolbar>
            <ion-title size="large">Camera Test</ion-title>
          </ion-toolbar>
        </ion-header>
      
        <div id="container">
          <ion-button @click="takeVideo" shape="circle">
            <ion-icon :md="icon.md" :ios="icon.ios"></ion-icon>
          </ion-button>
          <br/>
          <strong>Click the button</strong>
          <p> You<a target="_blank" rel="noopener noreferrer" href="https://www.google.com/"> Fool</a></p>
          <p>{{JSON.stringify(videoInfo)}}</p>
        </div>
  
      </ion-content>
    </ion-page>
  </template>
  
  <script>
  import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar, IonButton, IonIcon } from '@ionic/vue';
  import { defineComponent } from 'vue';
  import { cameraOutline  } from 'ionicons/icons';
  import {MediaCapture} from '@awesome-cordova-plugins/media-capture';
  import {Capacitor} from '@capacitor/core';
  import axios from 'axios';
  
  export default defineComponent({
    name: 'HomePage',
    components: {
      IonContent,
      IonIcon,
      IonButton,
      IonHeader,
      IonPage,
      IonTitle,
      IonToolbar
    },
    data() {
      return {
        videoInfo: {},
        icon: {
          md: cameraOutline,
          ios: cameraOutline
        }
      }
    },
    methods: {
      
      takeVideo: async function () {``
        
        try {
          const options = {
            duration: 10,
            limit: 1,
            quality: 1
          };
          const result = await MediaCapture.captureVideo(options);
          this.videoInfo = result[0];
          // console.log("videoInfo", JSON.stringify(result[0]));
          const blob = await fetch(
            Capacitor.convertFileSrc(this.videoInfo.fullPath)
          ).then(r => r.blob());
          const formData = new FormData();
          formData.append("file", blob, this.videoInfo.name);
          // convert video blob to base64
          let reader = new FileReader();
          reader.readAsDataURL(blob);
          reader.onloadend = async function() {
            let base64data = reader.result;
            let trimmed = base64data.substring(base64data.indexOf(",") + 1);
            console.log(trimmed);
          axios({
            method: "post",
            url: "https://51d1-2620-101-c040-85c-d08b-6896-278c-74d5.ngrok.io/upload/",
            data: JSON.stringify({
              _data: trimmed
            }),
          headers: {
            "Content-Type": "application/json"
          }
          }).then((response) => {
            alert(response.status);
          });
          };
        } catch (error) {
          alert(error);
      }
    }
  }
  });
  </script>
  
  <style scoped>
  #container {
    text-align: center;
    
    position: absolute;
    left: 0;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
  }
  
  #container strong {
    font-size: 20px;
    line-height: 26px;
  }
  
  #container p {
    font-size: 16px;
    line-height: 22px;
    
    color: #8c8c8c;
    
    margin: 0;
  }
  
  #container a {
    text-decoration: none;
  }
  ion-button [shape=circle] {
    border-radius: 100% !important;
    width: 56px;
    height: 56px;
  }
  </style>
  