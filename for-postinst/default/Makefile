PKG_SOURCE_URL:=${DL_MIRROR}/eng/nordic/download_resource/${PKG_IDENTIFIER}

DL_DIR=/var/cache/nrf5x-${PKG_NAME}-installer
INSTALL_DIR=/usr/lib/${INS_DIR}
DOC_DIR=/usr/share/doc/nrf5x-${PKG_NAME}

all: $(UNPACK_DIR)/source.properties

install: all
	$(eval UNPACK_DIR=$(DL_DIR)/extracted)
	install -d -m0755 $(DOC_DIR)
	@if [ -f $(UNPACK_DIR)source.properties ]; then \
		install -m0644 $(UNPACK_DIR)source.properties $(DOC_DIR)/ ; \
        fi
	@if [ -f $(UNPACK_DIR)NOTICE.txt ]; then \
		gzip -9 --stdout $(UNPACK_DIR)/NOTICE.txt > $(DOC_DIR)/copyright.gz ; \
        fi
	find ${DOC_DIR} | sort >> /var/lib/dpkg/info/nrf5x-${PKG_NAME}-installer.list
	chmod -R a+rX $(UNPACK_DIR)
	chmod -R go-w $(UNPACK_DIR)
	install -d -m0755 $(INSTALL_DIR)
	@if [ ! -d $(INSTALL_DIR)$(TRG_DIR) ]; then \
		mv $(UNPACK_DIR) $(INSTALL_DIR)${TRG_DIR}  ;\
		chown -R root:root $(INSTALL_DIR)${TRG_DIR} ;\
		find ${INSTALL_DIR}${TRG_DIR}  | sort >> /var/lib/dpkg/info/nrf5x-${PKG_NAME}-installer.list ;\
	else\
		echo "\033[0;31m$(INSTALL_DIR)${TRG_DIR} already exists.\033[0m" ; \
		exit 1 ; \
	fi

$(UNPACK_DIR)/source.properties: $(DL_DIR)/$(PKG_SOURCE)
	@if [ "$(findstring .tar,$(PKG_SOURCE))" = ".tar" ] ; then \
		cd $(DL_DIR) && mkdir -p extracted && cd extracted && tar -xvf $(DL_DIR)/$(PKG_SOURCE) ;\
	else \
		cd $(DL_DIR) && mkdir -p extracted && cd extracted && unzip -ou $(DL_DIR)/$(PKG_SOURCE) ; \
	fi

$(DL_DIR)/$(PKG_SOURCE):
	cd $(DL_DIR) && \
		su nobody -s /bin/sh -c "wget -O $(PKG_SOURCE) --continue $(PKG_SOURCE_URL)"
	sha256sum -c $(PKG_SOURCE).sha256

clean:
	-rm -rf -- $(UNPACK_DIR)

distclean: clean
	-rm -rf -- $(DL_DIR)

.PHONY: install clean