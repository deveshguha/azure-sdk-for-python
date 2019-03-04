# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class CustomVisionError(Model):
    """CustomVisionError.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. The error code. Possible values include: 'NoError',
     'BadRequest', 'BadRequestExceededBatchSize', 'BadRequestNotSupported',
     'BadRequestInvalidIds', 'BadRequestProjectName',
     'BadRequestProjectNameNotUnique', 'BadRequestProjectDescription',
     'BadRequestProjectUnknownDomain',
     'BadRequestProjectUnknownClassification',
     'BadRequestProjectUnsupportedDomainTypeChange',
     'BadRequestProjectUnsupportedExportPlatform', 'BadRequestIterationName',
     'BadRequestIterationNameNotUnique', 'BadRequestIterationDescription',
     'BadRequestIterationIsNotTrained', 'BadRequestWorkspaceCannotBeModified',
     'BadRequestWorkspaceNotDeletable', 'BadRequestTagName',
     'BadRequestTagNameNotUnique', 'BadRequestTagDescription',
     'BadRequestTagType', 'BadRequestMultipleNegativeTag',
     'BadRequestImageTags', 'BadRequestImageRegions',
     'BadRequestNegativeAndRegularTagOnSameImage',
     'BadRequestIterationIsPublished', 'BadRequestInvalidPublishName',
     'BadRequestSubscriptionApi', 'BadRequestPublishFailed',
     'BadRequestUnpublishFailed', 'BadRequestExceedProjectLimit',
     'BadRequestExceedIterationPerProjectLimit',
     'BadRequestExceedTagPerProjectLimit', 'BadRequestExceedTagPerImageLimit',
     'BadRequestExceededQuota', 'BadRequestCannotMigrateProjectWithName',
     'BadRequestNotLimitedTrial', 'BadRequestImageBatch',
     'BadRequestImageStream', 'BadRequestImageUrl', 'BadRequestImageFormat',
     'BadRequestImageSizeBytes', 'BadRequestImageExceededCount',
     'BadRequestTrainingNotNeeded',
     'BadRequestTrainingNotNeededButTrainingPipelineUpdated',
     'BadRequestTrainingValidationFailed',
     'BadRequestClassificationTrainingValidationFailed',
     'BadRequestMultiClassClassificationTrainingValidationFailed',
     'BadRequestMultiLabelClassificationTrainingValidationFailed',
     'BadRequestDetectionTrainingValidationFailed',
     'BadRequestTrainingAlreadyInProgress',
     'BadRequestDetectionTrainingNotAllowNegativeTag',
     'BadRequestInvalidEmailAddress', 'BadRequestBakingAlreadyInProgress',
     'BadRequestExportValidationFailed', 'BadRequestExportAlreadyInProgress',
     'BadRequestPredictionIdsMissing', 'BadRequestPredictionIdsExceededCount',
     'BadRequestPredictionTagsExceededCount',
     'BadRequestPredictionResultsExceededCount',
     'BadRequestPredictionInvalidApplicationName',
     'BadRequestPredictionInvalidQueryParameters', 'BadRequestInvalid',
     'UnsupportedMediaType', 'Forbidden', 'ForbiddenUser',
     'ForbiddenUserResource', 'ForbiddenUserSignupDisabled',
     'ForbiddenUserSignupAllowanceExceeded', 'ForbiddenUserDoesNotExist',
     'ForbiddenUserDisabled', 'ForbiddenUserInsufficientCapability',
     'ForbiddenDRModeEnabled', 'ForbiddenInvalid', 'NotFound',
     'NotFoundProject', 'NotFoundProjectDefaultIteration', 'NotFoundIteration',
     'NotFoundIterationPerformance', 'NotFoundTag', 'NotFoundImage',
     'NotFoundDomain', 'NotFoundApimSubscription', 'NotFoundInvalid',
     'Conflict', 'ConflictInvalid', 'ErrorUnknown',
     'ErrorProjectInvalidWorkspace',
     'ErrorProjectInvalidPipelineConfiguration', 'ErrorProjectInvalidDomain',
     'ErrorProjectTrainingRequestFailed', 'ErrorProjectExportRequestFailed',
     'ErrorFeaturizationServiceUnavailable', 'ErrorFeaturizationQueueTimeout',
     'ErrorFeaturizationInvalidFeaturizer',
     'ErrorFeaturizationAugmentationUnavailable',
     'ErrorFeaturizationUnrecognizedJob',
     'ErrorFeaturizationAugmentationError', 'ErrorExporterInvalidPlatform',
     'ErrorExporterInvalidFeaturizer', 'ErrorExporterInvalidClassifier',
     'ErrorPredictionServiceUnavailable', 'ErrorPredictionModelNotFound',
     'ErrorPredictionModelNotCached', 'ErrorPrediction',
     'ErrorPredictionStorage', 'ErrorRegionProposal', 'ErrorInvalid'
    :type code: str or
     ~azure.cognitiveservices.vision.customvision.prediction.models.CustomVisionErrorCodes
    :param message: Required. A message explaining the error reported by the
     service.
    :type message: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, code, message: str, **kwargs) -> None:
        super(CustomVisionError, self).__init__(**kwargs)
        self.code = code
        self.message = message


class CustomVisionErrorException(HttpOperationError):
    """Server responsed with exception of type: 'CustomVisionError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(CustomVisionErrorException, self).__init__(deserialize, response, 'CustomVisionError', *args)
