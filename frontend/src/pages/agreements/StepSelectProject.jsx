import React from "react";
import { useNavigate } from "react-router-dom";
import ProjectSelect from "../../components/UI/Form/ProjectSelect";
import StepIndicator from "../../components/UI/StepIndicator/StepIndicator";
import Modal from "../../components/UI/Modal";
import { useGetResearchProjectsQuery } from "../../api/opsAPI";
import { useCreateAgreement, useSetState, useUpdateAgreement } from "./CreateAgreementContext";
import EditModeTitle from "./EditModeTitle";

/**
 * Renders a step in the Create Agreement wizard for selecting a research project.
 *
 * @param {Object} props - The component props.
 * @param {Function} [props.goToNext] - A function to go to the next step in the wizard. - optional
 * @param {string} [props.formMode] - The mode of the form (e.g. "create", "edit", "review"). - optional
 * @returns {JSX.Element} - The rendered component.
 */
export const StepSelectProject = ({ goToNext, formMode }) => {
    const navigate = useNavigate();
    const { wizardSteps, selected_project: selectedResearchProject } = useCreateAgreement();
    // setters
    const setSelectedProject = useSetState("selected_project");
    const setAgreementProjectId = useUpdateAgreement("research_project_id");

    const [showModal, setShowModal] = React.useState(false);
    const [modalProps, setModalProps] = React.useState({});
    const [isEditMode, setIsEditMode] = React.useState(false);
    const { data: projects, error: errorProjects, isLoading: isLoadingProjects } = useGetResearchProjectsQuery();

    React.useEffect(() => {
        if (formMode === "edit" || formMode === "review") {
            setIsEditMode(true);
        }
    }, [formMode]);

    if (isLoadingProjects) {
        return <div>Loading...</div>;
    }
    if (errorProjects) {
        return <div>Oops, an error occurred</div>;
    }

    const handleContinue = () => {
        if (selectedResearchProject?.id) {
            goToNext({ project: selectedResearchProject.id });
        }
    };
    const handleCancel = () => {
        setShowModal(true);
        setModalProps({
            heading: "Are you sure you want to cancel? Your agreement will not be saved.",
            actionButtonText: "Cancel",
            secondaryButtonText: "Continue Editing",
            handleConfirm: () => {
                setModalProps({});
                navigate("/");
            },
        });
    };

    const handleAddProject = () => {
        navigate("/projects/create");
    };

    return (
        <>
            {showModal && (
                <Modal
                    heading={modalProps.heading}
                    setShowModal={setShowModal}
                    actionButtonText={modalProps.actionButtonText}
                    secondaryButtonText={modalProps.secondaryButtonText}
                    handleConfirm={modalProps.handleConfirm}
                />
            )}
            <EditModeTitle isEditMode={isEditMode} />
            <StepIndicator steps={wizardSteps} currentStep={1} />
            <h2 className="font-sans-lg">Select a Project</h2>
            <p>
                Select a project the agreement should be associated with. If you need to create a new project, click Add
                New Project.
            </p>
            <ProjectSelect
                researchProjects={projects}
                selectedResearchProject={selectedResearchProject}
                setSelectedProject={setSelectedProject}
                setAgreementProjectId={setAgreementProjectId}
            />
            <div className="grid-row flex-justify-end margin-top-8">
                <button
                    className="usa-button usa-button--unstyled margin-right-2"
                    data-cy="cancel-button"
                    onClick={handleCancel}
                >
                    Cancel
                </button>
                <button
                    id={"continue"}
                    className="usa-button"
                    onClick={handleContinue}
                    disabled={!selectedResearchProject?.id}
                >
                    Continue
                </button>
            </div>
            <div className="display-flex flex-align-center margin-top-6">
                <div className="border-bottom-1px border-base-light width-full" />
                <span className="text-base margin-left-2 margin-right-2">or</span>
                <div className="border-bottom-1px border-base-light width-full" />
            </div>
            <div className="grid-row flex-justify-center">
                <button
                    className="usa-button usa-button--outline margin-top-6 margin-bottom-6"
                    onClick={handleAddProject}
                >
                    Add New Project
                </button>
            </div>
        </>
    );
};

export default StepSelectProject;
