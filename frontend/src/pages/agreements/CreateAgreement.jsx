import CreateAgreementFlow from "./CreateAgreementFlow";
import StepSelectProject from "./StepSelectProject";
import StepCreateAgreement from "./StepCreateAgreement";
import { StepCreateBudgetLines } from "./StepCreateBudgetLines";
import StepAgreementSuccess from "../../components/UI/WizardSteps/StepCreateBudgetLines";
import { useCreateAgreement } from "./CreateAgreementContext";

export const CreateAgreement = () => {
    const createAgreementContext = useCreateAgreement();

    const {
        wizardSteps,
        selected_project: selectedResearchProject,
        selected_agreement: selectedAgreement,
        selected_procurement_shop: selectedProcurementShop,
        existing_budget_lines: existingBudgetLines,
    } = createAgreementContext;

    return (
        <CreateAgreementFlow>
            <StepSelectProject />
            <StepCreateAgreement />
            <StepCreateBudgetLines
                wizardSteps={wizardSteps}
                currentStep={3}
                selectedResearchProject={selectedResearchProject}
                selectedAgreement={selectedAgreement}
                selectedProcurementShop={selectedProcurementShop}
                existingBudgetLines={existingBudgetLines}
            />
            <StepAgreementSuccess />
        </CreateAgreementFlow>
    );
};

export default CreateAgreement;
