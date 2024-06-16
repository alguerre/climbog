import "./Footer.css"
import climber_ico from "./assets/climber-ico.svg";

function Footer() {
    return (
        <footer>
            <div><strong>CLIMB MORE</strong></div>
            <div><img src={climber_ico} alt="Footer Icon"/></div>
            <div><strong>WORK LESS</strong></div>
        </footer>
    )
}

export default Footer;
