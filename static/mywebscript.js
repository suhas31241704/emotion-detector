function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function () {
        document.getElementById("system_response").innerHTML = this.responseText;
    };
    xhttp.open("GET", "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze));
    xhttp.send();
}