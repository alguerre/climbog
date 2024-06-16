import './App.css';
import NavBar from "./NavBar";
import { BrowserRouter as Router } from 'react-router-dom';
import Footer from "./Footer";


function App() {
    return (
        <Router>
            <div className="App">
                <NavBar />
                {/* Main is included in NavBar with routes */}
                <Footer />
            </div>
        </Router>
    );
}

export default App;
