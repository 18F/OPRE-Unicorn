import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { redirect } from "react-router-dom";
import StepIndicator from "../../components/UI/StepIndicator/StepIndicator";
import { ProjectAgreementSummaryCard } from "../budgetLines/ProjectAgreementSummaryCard";
import PreviewTable from "../budgetLines/PreviewTable";
import { Alert } from "../../components/UI/Alert/Alert";
import { Modal } from "../../components/UI/Modal/Modal";
import CreateBudgetLinesForm from "../../components/UI/Form/CreateBudgetLinesForm";
import {
    setBudgetLineAdded,
    setEnteredDescription,
    setEnteredAmount,
    setEnteredMonth,
    setEnteredYear,
    setEnteredDay,
    setEnteredComments,
    deleteBudgetLineAdded,
} from "../budgetLines/createBudgetLineSlice";
import { setSelectedProcurementShop } from "../agreements/createAgreementSlice";
import { postBudgetLineItems } from "../../api/postBudgetLineItems";

export const StepCreateBudgetLines = ({ goBack, goToNext, wizardSteps }) => {
    const dispatch = useDispatch();
    const budgetLinesAdded = useSelector((state) => state.createBudgetLine.budget_lines_added);
    const selectedProcurementShop = useSelector((state) => state.createAgreement.selected_procurement_shop);
    const selectedResearchProject = useSelector((state) => state.createAgreement.selected_project);
    const selectedAgreement = useSelector((state) => state.createAgreement.agreement);
    const [isAlertActive, setIsAlertActive] = React.useState(false);
    const [alertProps, setAlertProps] = React.useState({});
    const [showModal, setShowModal] = React.useState(false);
    const [modalProps, setModalProps] = React.useState({});

    const showAlert = async (type, heading, message) => {
        await new Promise((resolve) => setTimeout(resolve, 500));
        window.scrollTo(0, 0);
        setIsAlertActive(true);
        setAlertProps({ type, heading, message });

        await new Promise((resolve) => setTimeout(resolve, 6000));
        setIsAlertActive(false);
        setAlertProps({});
    };

    const handleDeleteBudgetLine = (budgetLineId) => {
        setShowModal(true);
        setModalProps({
            heading: "Are you sure you want to delete this budget line?",
            actionButtonText: "Delete",
            handleConfirm: () => {
                dispatch(deleteBudgetLineAdded(budgetLineId));
                showAlert("success", "Budget Line Deleted", "The budget line has been successfully deleted.");
                setModalProps({});
            },
        });
    };

    const saveBudgetLineItems = (event) => {
        event.preventDefault();
        const newBudgetLineItems = budgetLinesAdded.filter(
            // eslint-disable-next-line no-prototype-builtins
            (budgetLineItem) => !budgetLineItem.hasOwnProperty("created_on")
        );
        postBudgetLineItems(newBudgetLineItems).then(() => console.log("Created New BLIs."));
        // TODO: Route to Agreements List page, showing Agreement Review for now
        redirect("/agreements/");
        // goToNext();
    };

    return (
        <>
            {showModal && (
                <Modal
                    heading={modalProps.heading}
                    setShowModal={setShowModal}
                    actionButtonText={modalProps.actionButtonText}
                    handleConfirm={modalProps.handleConfirm}
                />
            )}

            {isAlertActive ? (
                <Alert heading={alertProps.heading} type={alertProps.type} setIsAlertActive={setIsAlertActive}>
                    {alertProps.message}
                </Alert>
            ) : (
                <>
                    <h1 className="font-sans-lg">Create New Budget Line</h1>
                    <p>Step Two: Text explaining this page</p>
                </>
            )}
            <StepIndicator steps={wizardSteps} currentStep={3} />
            <ProjectAgreementSummaryCard
                selectedResearchProject={selectedResearchProject}
                selectedAgreement={selectedAgreement}
                selectedProcurementShop={selectedProcurementShop}
            />
            <h2 className="font-sans-lg margin-top-3">Budget Line Details</h2>
            <p>
                Complete the information below to create new budget lines. Select Add Budget Line to create multiple
                budget lines.
            </p>
            <CreateBudgetLinesForm
                selectedAgreement={selectedAgreement}
                selectedProcurementShop={selectedProcurementShop}
                showAlert={showAlert}
            />
            <h2 className="font-sans-lg">Budget Lines</h2>
            <p>
                This is a list of all budget lines for the selected project and agreement. The budget lines you add will
                display in draft status. The Fiscal Year (FY) will populate based on the election date you provide.
            </p>

            <PreviewTable handleDeleteBudgetLine={handleDeleteBudgetLine} />
            <div className="grid-row flex-justify-end margin-top-1">
                <button
                    className="usa-button usa-button--unstyled margin-right-2"
                    onClick={() => {
                        // if no budget lines have been added, go back
                        if (budgetLinesAdded.length === 0) {
                            goBack();
                            return;
                        }
                        // if budget lines have been added, show modal
                        setShowModal(true);
                        setModalProps({
                            heading: "Are you sure you want to go back? Your budget lines will not be saved.",
                            actionButtonText: "Go Back",
                            handleConfirm: () => {
                                dispatch(setBudgetLineAdded([]));
                                dispatch(setEnteredAmount(null));
                                dispatch(setEnteredComments(""));
                                dispatch(setEnteredDescription(""));
                                dispatch(setSelectedProcurementShop(-1));
                                dispatch(setEnteredDay(""));
                                dispatch(setEnteredMonth(""));
                                dispatch(setEnteredYear(""));
                                setModalProps({});
                                goBack();
                            },
                        });
                    }}
                >
                    Back
                </button>
                <button className="usa-button" onClick={saveBudgetLineItems}>
                    Continue
                </button>
            </div>
        </>
    );
};
