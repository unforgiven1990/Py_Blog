import(
      "https://storage.googleapis.com/speechify-api-cdn/speechifyapi.min.mjs"
    ).then(async (speechifyWidget) => {
      // this parent element for your article or listenable content
      const articleRootElement = document.querySelector("#main");
      // this is the header of your article; the inline player will be placed under this heading
      const articleHeading = articleRootElement.querySelector("#time");

      const widget = speechifyWidget.makeSpeechifyExperience({
        rootElement: articleRootElement,
        inlinePlayerElement: articleHeading,
      });
      await widget.mount();
    });