import { useState } from "react";

import "./App.css";

import Navbar from "./components/Navbar/Navbar";
import Sidebar from "./components/Sidebar/Sidebar";
import Hero from "./components/Hero/Hero";
import VoiceCard from "./components/VoiceCard/VoiceCard";
import WeatherCard from "./components/WeatherCard/WeatherCard";
import AnalysisCard from "./components/AnalysisCard/AnalysisCard";
import ResponseCard from "./components/ResponseCard/ResponseCard";
import ChartGallery from "./components/ChartGallery/ChartGallery";
import PDFCard from "./components/PDFCard/PDFCard";
import Footer from "./components/Footer/Footer";

function App() {

  const [analysisData, setAnalysisData] = useState(null);

  return (

    <>

      <Navbar />

      <div className="container">

        <Sidebar />

        <main className="content">

          <Hero />

          <VoiceCard />

          <div className="cards">

            <WeatherCard />

            <AnalysisCard setAnalysisData={setAnalysisData} />

          </div>

          <ResponseCard report={analysisData?.report} />

          <ChartGallery charts={analysisData?.charts} />

          <PDFCard pdf={analysisData?.pdf} />

          <Footer />

        </main>

      </div>

    </>

  );

}

export default App;