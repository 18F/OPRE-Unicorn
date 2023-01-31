import styles from "./styles.module.css";
import CurrencyWithSmallCents from "../../UI/CurrencyWithSmallCents/CurrencyWithSmallCents";
import CANFundingBar from "../CANFundingBar/CANFundingBar";

const CANFundingYTD = ({ current_funding, expected_funding, className = "" }) => {
    const gridRowText = `grid-row padding-top-1 ${styles.gridRowText}`;

    return (
        <div className={className}>
            <div className="grid-row">
                <div className="grid-col-3">
                    <CurrencyWithSmallCents
                        amount={current_funding || 0}
                        dollarsClasses="font-sans-3xs text-bold"
                        centsStyles={{ fontSize: "8px" }}
                    />
                </div>
                <div className="grid-col-3 grid-offset-6">
                    <div className={styles.right}>
                        <CurrencyWithSmallCents
                            amount={expected_funding || 0}
                            dollarsClasses="font-sans-3xs text-bold"
                            centsStyles={{ fontSize: "8px" }}
                        />
                    </div>
                </div>
            </div>
            <div className={styles.barBox}>
                <CANFundingBar current_funding={current_funding} expected_funding={expected_funding} />
            </div>
            <div className={gridRowText}>
                <div className="grid-col-2">
                    <span>Received</span>
                </div>
                <div className="grid-col-2 grid-offset-8">
                    <span className={styles.right}>Expected</span>
                </div>
            </div>
        </div>
    );
};

export default CANFundingYTD;
