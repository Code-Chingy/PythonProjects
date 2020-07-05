import logging

from utils.base.processors.null_processor import NullProcessor
from utils.base.processors.assignment_processor import AssignmentProcessor
from utils.base.processors.identifier_processor import IdentifierProcessor
from utils.base.processors.object_processors import StringProcessor, NumberProcessor
from utils.base.processors.syntax_processors import SyntaxHelperProcessor, RunProcessor

logging.basicConfig(format="%(levelname)-8s [%(filename)s:%(lineno)d] %(message)s", level=logging.DEBUG)
# logging.disable(logging.DEBUG)
logger = logging.getLogger(__name__)

WORD_PROCESSORS = {
    '': NullProcessor,
    'operator.=': AssignmentProcessor,
    'operator.+': NullProcessor,
    'operator.-': NullProcessor,
    'operator.*': NullProcessor,
    'operator./': NullProcessor,
    'operator.%': NullProcessor,
    'operator.&': NullProcessor,
    'operator.~': NullProcessor,
    'operator.^': NullProcessor,
    'operator.++': NullProcessor,
    'operator.--': NullProcessor,
    'operator.//': NullProcessor,
    'operator.**': NullProcessor,
    'operator.+=': NullProcessor,
    'operator.-=': NullProcessor,
    'operator.*=': NullProcessor,
    'operator./=': NullProcessor,
    'operator.%=': NullProcessor,
    'operator.//=': NullProcessor,
    'operator.**=': NullProcessor,
    'operator.>': NullProcessor,
    'operator.<': NullProcessor,
    'operator.!': NullProcessor,
    'operator.==': NullProcessor,
    'operator.<=': NullProcessor,
    'operator.>=': NullProcessor,
    'operator.!=': NullProcessor,
    'operator.accessor': NullProcessor,
    'expression.helper.#': SyntaxHelperProcessor,
    'expression.helper.:': SyntaxHelperProcessor,
    'expression.helper.;': SyntaxHelperProcessor,
    'expression.helper.,': SyntaxHelperProcessor,
    'expression.helper.$': SyntaxHelperProcessor,
    'expression.helper.@': SyntaxHelperProcessor,
    'expression.helper.?': SyntaxHelperProcessor,
    'expression.helper.|': SyntaxHelperProcessor,
    'expression.helper.\\': SyntaxHelperProcessor,
    'expression.helper.run': RunProcessor,
    'data.identifier': IdentifierProcessor,
    'builtins.class': NullProcessor,
    'builtins.object': NullProcessor,
    'builtins.data.byte': NullProcessor,
    'builtins.data.bool': NullProcessor,
    'builtins.data.list': NullProcessor,
    'builtins.data.dict': NullProcessor,
    'builtins.data.set': NullProcessor,
    'builtins.data.tuple': NullProcessor,
    'builtins.data.object': NullProcessor,
    'builtins.data.string': StringProcessor,
    'builtins.data.number': NumberProcessor,
    'builtins.data.number.float': NumberProcessor,
    'builtins.data.number.integer': NumberProcessor,
    'builtins.keyword.if': NullProcessor,
    'builtins.keyword.else': NullProcessor,
    'builtins.keyword.elseif': NullProcessor,
    'builtins.keyword.while': NullProcessor,
    'builtins.keyword.switch': NullProcessor,
    'builtins.keyword.case': NullProcessor,
    'builtins.keyword.for': NullProcessor,
    'builtins.keyword.in': NullProcessor,
    'builtins.keyword.is': NullProcessor,
    'builtins.keyword.not': NullProcessor,
    'builtins.keyword.as': NullProcessor,
    'builtins.keyword.from': NullProcessor,
    'builtins.keyword.with': NullProcessor,
    'builtins.keyword.whenever': NullProcessor,
    'builtins.keyword.do': NullProcessor,
    'builtins.keyword.of': NullProcessor,
    'builtins.keyword.then': NullProcessor,
    'builtins.keyword.when': NullProcessor,
    'builtins.keyword.try': NullProcessor,
    'builtins.keyword.catch': NullProcessor,
    'builtins.keyword.except': NullProcessor,
    'builtins.keyword.continue': NullProcessor,
    'builtins.keyword.break': NullProcessor,
    'builtins.keyword.new': NullProcessor,
    'builtins.keyword.async': NullProcessor,
    'builtins.keyword.await': NullProcessor,
    'builtins.keyword.self': NullProcessor,
    'builtins.keyword.this': NullProcessor,
    'builtins.keyword.ref': NullProcessor,
    'builtins.keyword.func': NullProcessor,
    'builtins.keyword.const': NullProcessor,
    'builtins.keyword.final': NullProcessor,
    'builtins.keyword.static': NullProcessor,
    'builtins.keyword.private': NullProcessor,
    'builtins.keyword.public': NullProcessor,
    'builtins.keyword.protected': NullProcessor,
    'builtins.keyword.interface': NullProcessor,
    'builtins.keyword.abstract': NullProcessor,
    'builtins.keyword.extends': NullProcessor,
    'builtins.keyword.implements': NullProcessor,
    'builtins.keyword.foreach': NullProcessor,
    'builtins.keyword.return': NullProcessor,
    'builtins.keyword.class': NullProcessor,
    'builtins.keyword.endforeach': NullProcessor,
    'builtins.keyword.endif': NullProcessor,
    'builtins.keyword.endwhile': NullProcessor,
    'builtins.keyword.endfor': NullProcessor,
    'builtins.keyword.endwith': NullProcessor,
    'builtins.keyword.endswitch': NullProcessor,
    'builtins.keyword.endfunc': NullProcessor,
    'builtins.keyword.endclass': NullProcessor,
    'builtins.keyword.import': NullProcessor,
    'builtins.keyword.export': NullProcessor,
    'builtins.keyword.include': NullProcessor,
    'builtins.keyword.require': NullProcessor,
    'expression.collection.opener.(': SyntaxHelperProcessor,
    'expression.collection.opener.{': SyntaxHelperProcessor,
    'expression.collection.opener.[': SyntaxHelperProcessor,
    'expression.collection.closer.)': SyntaxHelperProcessor,
    'expression.collection.closer.}': SyntaxHelperProcessor,
    'expression.collection.closer.]': SyntaxHelperProcessor
}


def generate_word_processor(i, word):
    logger.debug(f'{word}')
    try:
        return WORD_PROCESSORS[f'{word.get_type()}'](i, word)
    except TypeError:
        return WORD_PROCESSORS[f'{word.get_type()}'](i)
    except KeyError as e:
        logger.debug(e)
