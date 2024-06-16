import stones_ico from './assets/stones-ico.svg';
import { NavLink, Route, Routes } from 'react-router-dom';
import './NavBar.css';

function NavBar() {
    return (
        <>
            <nav className="navbar navcontainer">
                <img src={stones_ico} alt="Stones Icon"/>
                <NavLink to="/" activeClassName="active">Home</NavLink>
                <NavLink to="/calendar"  activeClassName="active">Calendar</NavLink>
            </nav>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/calendar" element={<Calendar />} />
            </Routes>
        </>
    );
}

function Home() {
    return <h1>Home</h1>;
}

function Calendar() {
    return <h1>Calendar</h1>;
}

export default NavBar;